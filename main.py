import smith_wunsch as sm_wun
import consensus_alignment as cnsus
import PSSM as pssm

def sm_wun_auto():
    str1 = "TGCTCGTA"     ## 5 -2 -6
    # str1 = "TGTTACGG"      ## 5 -2 -6
    # str1 = "CGTGAATTCAT"  ## +5,-3, -4
    # str1 = "GCATGCG"  ## 1 -1 -1
    # str1 = "TACGGGCCCGCTAC"  ## 5 -2 -3
    # str1 = "cgggtatccaa".upper()
    str1 = "ACGCTG"
    # str1 = "GWAAPHETA"
    # str1 = "TCTCGAT"
    # str1 = "GAHCDFE"
    # str1 = "ACGCTG"
    # str1 = "ccgtacta".upper()

    # str2 = "TTCATA"
    # str2 = "GGTTGACTA"
    # str2 = "GACTTAC"
    # str2 = "GATTACA"
    # str2 = "TAGCCCTATCGGTCA"
    # str2 = "ccctaggtccca".upper()
    str2 = "CATGT"
    # str2 = "TWAAHEGG"
    # str2 = "GTCTAC"
    # str2 = "ACDEF"
    # str2 = "CATGT"
    # str2 = "cagaccta".upper()

    config = {
        "algo": "needleman_wunsch", "type": "dna", "scoring": "dna", "match": 2, "mismatch": -1, "gap": -1,
    }

    # config = {
    #     "algo": "smith_waterman", "type": "protein", "scoring": "pam", "match": 2, "mismatch": -1, "gap": -1,
    # }
    sm_wun.smith_wunsch(str1, str2, config)

def sm_wun_input():
    str1 = input("Enter 1st sequence\n").replace("\"", "")
    str2 = input("Enter 2nd sequence\n").replace("\"", "")
    config = {"algo": input("Enter which algorithm [needleman_wunsch | smith_waterman]\n").strip(),
              "type": input("Enter sequence type [dna | protein]\n").strip(), "scoring": "dna",}
    if config["type"] == "protein":
        config["scoring"] = input("Enter scoring matrix [pam | blosum]\n").strip()
        config["gap"] = int(input("Enter gap\n").strip())
        sm_wun.smith_wunsch(str1, str2, config)
        print("heyy")
        return
    config["match"] = int(input("Enter match\n").strip())
    config["mismatch"] = int(input("Enter mismatch\n").strip())
    config["gap"] = int(input("Enter gap\n").strip())
    sm_wun.smith_wunsch(str1, str2, config)

def cnsus_auto():
    strings = [
         "VTISCTGSSSNIGAG-NHVKWYQQLPG", "VTISCTGTSSNIGS--ITVNWYQQSPG", "LRLSCSSSGFIFSS--YAMYWVRQAPG", "LSLTCTVSGTSFDD--YYSTWVRQPPG", "PEVTCVVVDVSHEDPQVKFNWYVDG--", "ATLVCLISDFYPGA--VTVAWKADSP-", "ATLVCLISDFYPGA--VTVAWKADS--", "AALGCLVKDYFPEP--VTVSWNQG---", "VSLTCLVKGFYPSD--IAVEWEQNG--"
    ]

    # strings = [
    #  "AGCGTGACTTCCAATAT", "TCGCACAAATAGTGTCT", "AACAAGCCATTCACCGC", "GGATGAACATGACTACG", "CCGGTTACACATTAGTA", "TAACCCGTCTGCCGAAA", "ATTACGACAACGGCCTC", "GTTTGAACGTGGGTCGG"
    # ]

    # strings = [
    #     "ATATTATG", "GTACTTTG", "TCACAGTA", "TTAGTCTC", "CTAACTTC"
    # ]

    # strings = [
    #      "FSTAAFRFGHATVHPLVRRLNT", "FSTAAFRFGHATVHPLVRRLNT", "FSTAAFRFGHATIHPLVRRLDA", "FSTAAFRFGHATIHPLVRRLDA", "FSTAAFRFGHATVHPLVRRLDA", "FATAAFRFGHATIQPIVRRLNA", "FTTAAFRFGHATIPPMVHRLDS"
    # ]

    #### test cases ####
    cnsus.get_all(cnsus.threshold_consensus, strings, 35 / 100)
    # cnsus.get_all(cnsus.sum_consensus, strings)
    # print(cnsus.threshold_consensus(strings, 20/100))
    # print(cnsus.threshold_consensus(strings, 40/100))
    # print(cnsus.threshold_consensus(strings, 70/100))
    # print(cnsus.threshold_consensus(strings, 100/100))
    # print(cnsus.sum_consensus(strings))

def cnsus_input():
    strings = input("Enter Sequences separated by a comma\n").replace('\"', '').replace(" ", "").split(",")
    method = input("Enter consensus method [threshold | sum]\n").replace(" ", "")
    if method == "threshold":
        threshold = float(eval(input("Enter preferred threshold\n")))
        cnsus.get_all(cnsus.threshold_consensus, strings, threshold)
    else:
        cnsus.get_all(cnsus.sum_consensus, strings)

def pssm_auto():
    strings = [
        "ATGTCG", "AAGACT", "TACTCA", "CGGAGG", "AACCTG"
    ]
    #
    # strings = [
    #      "AATTGA", "AGGTCC", "AGGATG", "AGGCGT"
    # ]

    # previous final question
    # strings = [
    #     "GAGGTAAAC", "TCCGTAAGT", "CAGGTTGGA", "ACAGTCAGT", "TAGGTCATT", "TAGGTACTG", "ATGGTAACT", "CAGGTATAC", "TGTGTGAGT", "AAGGTAAGT"
    # ]

    pssm.PSSM(strings, "AACTCG")
    # pssm.PSSM(strings, "CAGGTAAGT")
    # pssm.PSSM(strings, "GGAGTGGAG")
    # pssm.PSSM(strings, "GGTGTGGAG")
    # pssm.PSSM(strings, "GGAGTGGTG")
    # pssm.PSSM(strings, "GGTGTGGTG")

def pssm_input():
    strings = input("Enter Sequences separated by a comma\n").replace('\"', '').replace(" ", "").split(",")
    str_to_match = input("Enter the sequence to match with PSSM\n").replace('\"', "").replace(" ", "")
    pssm.PSSM(strings, str_to_match)


sm_wun_auto()
print("######################################")
# sm_wun_input()
cnsus_auto()
print("######################################")
# cnsus_input()
pssm_auto()
# pssm_input()
