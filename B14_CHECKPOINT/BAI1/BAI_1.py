class LaBai:
    def __init__(self, gia_tri, chat):
        self.gia_tri = gia_tri
        self.chat = chat
    def __str__(self):
        return f"{self.gia_tri} {self.chat}"
class BoBai:
    def __init__(self):
        self.cac_la_bai = []
        cac_chat = ["cơ", "rô", "tép", "bích"]
        cac_gia_tri = ["át( A )", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        for chat in cac_chat:
            for gia_tri in cac_gia_tri:
                self.cac_la_bai.append(LaBai(gia_tri, chat))
    def __str__(self):
        result = ""
        for la in self.cac_la_bai:
            result += str(la) + ", "
        return result.strip(", ")
#thần bài phát bài!!!!!!!!!!
bo = BoBai()
print(bo)
