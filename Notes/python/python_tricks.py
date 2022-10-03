* sys.maxsize #max size pc supports
* walrus operator , assigns and return at the same time
    while (a:=input())!=' ':
        print(a)

* a = [1,2,3]
    use, *a rather than ,print(' '.join(map(str,a)))


* a = [1,2,3]
    def create_phone_number(n):
        return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)
