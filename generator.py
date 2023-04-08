import itertools

passwords = []

def generate(keywords): 

    for i in keywords:
        nums = list(i) # separates the word in its letters
        permutations = list(itertools.permutations(nums))
        for permutation in permutations:
            passwords.append(''.join(permutation)) # join ('h', 'o', 'l', 'a') into 'hola'
    passwords.count()

    try:
        # TODO: verificar si existe el archivo, si existe, preguntar si eliminarlo o ponerle otro nombre
        f = open("%s_passgen.txt" % keywords[0], "at")
        for i in passwords:
            f.write("%s\n" % i)
    except Exception as e:
        print(e)