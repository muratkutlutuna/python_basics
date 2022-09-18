import re
# result = dir(re)
#['A', 'ASCII', 'DEBUG', 'DOTALL', 'I', 'IGNORECASE', 'L', 'LOCALE', 'M',
# 'MULTILINE', 'Match', 'Pattern', 'RegexFlag', 'S', 'Scanner', 'T', 'TEMPLATE',
# 'U', 'UNICODE', 'VERBOSE', 'X', '_MAXCACHE', '__all__', '__builtins__', '__cached__',
# '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '__version__',
# '_cache', '_compile', '_compile_repl', '_expand', '_locale', '_pickle',
# '_special_chars_map', '_subx', 'compile', 'copyreg', 'enum', 'error', 'escape', 'findall',
# 'finditer', 'fullmatch', 'functools', 'match', 'purge', 'search', 'split',
# 'sre_compile', 'sre_parse', 'sub', 'subn', 'template']
# print(result)

# re module

str = "Python Kursu: Python Programlama Rehberiniz | 40 saat"

# re.findall()

# result = re.findall("Python",str)
# print(f'{len(result)} adet {result[0]} var')

# re.split()

# result = re.split(" ", str)
# result = re.split("r", str)

# re.sub()

# result = re.sub(" ","-",str) # Python-Kursu:-Python-Programlama-Rehberiniz-|-40-saat
# result = re.sub("\s","-",str) # Python-Kursu:-Python-Programlama-Rehberiniz-|-40-saat
# print(result)

# search = re.search("Python", str)
# print(search) # <re.Match object; span=(0, 6), match='Python'> 0inci karakterden 6ya kadar
#                 # buldugunu ifade ediyor
# span = search.span()
# print(span)
# start = search.start()
# print(start)
# end = search.end()
# print(end)
# group = search.group()
# print(group)
# string = search.string
# print(string)

# regular expression

"""

    [] - koseli parantezler arasina yazilan butun karakterler aranir.
    
        [abc] => a      : 1 match
                 b      : 2 match
                 Python : No matches
                 
        [a-e] => [abcde]
        [1-5] => [12345]
        [0-39]=> [01239]
        
        [^abc]=> abc disindaki karakterler.
        [^0-9]=> rakam olmayan karakterler.
        
"""

# findall = re.findall("[abc]", str)
# print(findall)
# findall = re.findall('[sat]',str)
# print(findall)
# findall = re.findall('[a-e]',str)
# print(findall)
# findall = re.findall('[a-z]',str)
# print(findall)
# findall = re.findall('[0-5]',str)
# print(findall)

"""
    . - bir nokta, her hangi bir tek karakteri belirtir.
    
        .. =>   a       : No match (iki nokta herhangi iki basamakli ifadeyi arar
                ab      : 1 match
                abc     : 1 match
                abcd    : 2 matches    
"""
findall = re.findall("...", str)
print(findall)
findall = re.findall("Py..on", str)
print(findall)
'''
    ^ - Belirtilen karakterlerle stringin tamami basliyor mu?
    
    ^a  =>  a:      1 match
            abc:    1 match
            bac:    No match
'''
# result = re.findall("^P",str)
# print(result)
# result = re.findall("^a",str)
# print(result)
'''
    $ - Belirtilen karakterlerle bitiyor mu?

    a$  =>  a:      1 match
            lamba:  1 match
            Python: No match
            
'''
# result = re.findall("t$",str)
# print(result)
# result = re.findall("saat$",str)
# print(result)
# result = re.findall("s$",str)
# print(result)
'''
    * - Bir karakterin sifir ya da daha fazla sayida olmasini kontrol eder.
        
        ma*n    =>  mn      : 1 match
                    man     : 1 match
                    maaaan  : 1 match
                    main    : No match (a'nin arkasina n gelmiyor.)
'''
result = re.findall("sa*t",str)
print(result)
'''
    + - Bir karakterin bir ya da daha fazla sayida olmasini kontrol eder.
        
        ma+n    =>  mn      : No match
                    man     : 1 match
                    maaaan  : 1 match
                    main    : No match (a'nin arkasina n gelmiyor.)
'''
result = re.findall("sa+t",str)
print(result)
"""
    ? - Bir karakterin sifir ya da bir kez olmasini kontrol eder.
        
        ma?n    =>  mn      : No match
                    man     : 1 match
                    maaaan  : 1 match
                    main    : No match (a'nin arkasina n gelmiyor.)
"""
result = re.findall("sa?t",str)
print(result)
result = re.findall("saa?t",str)
print(result)
'''
    {} = Karater sayisini kontrol eder.
        
        al{2}       => a karakterlerinin arkasina l karakteri 2 kez tekrarlamali.
        al{2,3}     => a karakterinin arkasina l karakteri en az 2 en fazla 3 kez tekrarlamali
        [0-9]{2,4}  => en az 2 en cok 4 basamakli sayilar.
'''
result = re.findall("a{1}",str)
print(result)
result = re.findall("a{1,2}",str)
print(result)
result = re.findall("[a-z]{3,4}",str)
print(result)
"""
    | - alternatif seceneklerden birinin gerceklesmesi gerekir.
    
        a|n => a ya da b
        
            cde =>      no match
            ade =>      1 match
            acdbea =>   3 match
"""
result = re.findall("a|n",str)
print(result)
'''
    () - gruplamak icin kullanilir.
    
        (a|b|c)xz => a,b,c karakterlerinin arkasina xz gelmelidir.
'''
result = re.findall("\APython",str)
print(result)
result = re.findall("saat\Z",str)
print(result)
"""
    \ - ozel karakterleri aramamizi saglar.
        \$a => $ karkatelerinin arkasina a karakterinin arar. Yani
               $ regular exp. engine tarafindan yorumlanmaz.
    
    \A - Belirtilen karakter string in basinda mi?
        \Athe => the string in basindami
    
    \Z - Belirtilen karakter string in sonunda mi ?
        the\Z => the string in sonunda mi
        
    \b - belirtilen karakter kelimenin basinda ya da sonunda mi?
        \bthe => the kelimenin basinda mi?
        the\b => the kelimenin sonunda mi
        
    \B - belirtilen karakter kelimenin basinda ya da sonunda degil mi?
        \Bthe => the kelimenin basinda degil mi?
        the\B => the kelimenin sonunda degil mi?
        
    \d - [0-9] ile ayni anlama gelir yani rakamlari arar.
        \d => 12abc34
        
    \D - [^0-9] ile ayni anlama gelir yani rakam olmayanlari arar.
        \D => 1ab44_50
        
    \s - Bosluk karakterlerini arar.
    \S - Bosluk karakterleri disindakiler.
    \w - Alfabetik karakterler, rakamlar ve alt cizgi karakteri.
    \W - \w nun tam tersi
        
"""







