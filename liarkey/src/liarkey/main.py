from data import Sisters, Reliability, Possibility

# =========================================
# 初期状態の定義
# =========================================

# 姉妹に対する信頼性を初期化（マデリンは嘘つき、他は不明）
reliability_map: dict[Sisters, Reliability] = {sister: Reliability() for sister in list(Sisters)}
reliability_map[Sisters.MADELINE] = Reliability(liar=True)

def print_reliability():
    print("RELIABILITY")
    for sister, reliability in reliability_map.items():
        print(sister, reliability.get_name())
    print()

# 姉妹に対する犯行可能性を初期化（全員不明）
possibility_map: dict[Sisters, Possibility] = {sister: Possibility() for sister in list(Sisters)}

def print_possibility():
    print("POSSIBILITY")
    for sister, possibility in possibility_map.items():
        print(sister, possibility.get_name())
    print()

print_reliability()
print_possibility()


# =========================================
# 嘘つき者の調査
# =========================================

# 事前に各証言を言語化（True: 正直者, False: 嘘つき者）
testimony_reliability_map: dict[Sisters, dict[Sisters, bool]] = {
    Sisters.MABEL: { Sisters.DOROTHY: True },
    Sisters.DOROTHY: { Sisters.JULIETTA: False },
    Sisters.JULIETTA: { Sisters.ISABELLA: True },
    Sisters.ISABELLA: { Sisters.MADELINE: False },
    Sisters.MADELINE: { Sisters.MABEL: True }
}

# 信頼性がすべて明かされるまで調査（全射であるため）
while any(reliability.is_unknown() for reliability in reliability_map.values()):
    # print_reliability() # DEBUG
    for from_sister, from_reliability in reliability_map.items():
        for to_sister, judge in testimony_reliability_map[from_sister].items():
            # 正直者
            if judge:
                if from_reliability.is_truth_teller():
                    reliability_map[to_sister].truth_teller = True
                elif from_reliability.is_liar():
                    reliability_map[to_sister].liar = True
            # 嘘つき者
            else:
                if from_reliability.is_truth_teller():
                    reliability_map[to_sister].liar = True
                elif from_reliability.is_liar():
                    reliability_map[to_sister].truth_teller = True

print_reliability()


# =========================================
# 犯人の調査
# =========================================

# 事前に各証言を言語化（True: 犯人, False: 無実の者）
testimony_possibility_map: dict[Sisters, dict[Sisters, bool]] = {
    Sisters.MABEL: { Sisters.MADELINE: True },
    Sisters.DOROTHY: { Sisters.MABEL: True },
    Sisters.JULIETTA: { Sisters.DOROTHY: False },
    Sisters.ISABELLA: { Sisters.MADELINE: False },
    Sisters.MADELINE: { Sisters.JULIETTA: True }
}

for from_sister, from_reliability in reliability_map.items():
    for to_sister, to_possibility in testimony_possibility_map[from_sister].items():
        # 犯人である
        if testimony_possibility_map[from_sister][to_sister]:
            if from_reliability.is_truth_teller():
                possibility_map[to_sister].crimer = True
            elif from_reliability.is_liar():
                possibility_map[to_sister].innocence = True           
        # 無実である
        elif not testimony_possibility_map[from_sister][to_sister]:
            if from_reliability.is_truth_teller():
                possibility_map[to_sister].innocence = True
            elif from_reliability.is_liar():
                possibility_map[to_sister].crimer = True           

print_possibility()