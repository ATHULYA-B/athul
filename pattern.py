class pattern:
    def print_pattern(self,n):
        for i in range(n):
            line='0'
            for j in range(1,i+2):
                line+=str(j)
            if i>1:
                line+-line[-2::-1]
            print(line.1just(2*n))
pattern=pattern()
pattern.print_pattern(6)