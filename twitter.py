class Party:
    val = 0

    def __init__(self):
        print(self.val+1)

    def __del__(self):
        print(self.val-1)
    

party = Party()