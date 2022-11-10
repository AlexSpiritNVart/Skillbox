# user_input = input('Введите текст   ').lower()
user_input = 'vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj scfuuf ibou fy/dpnqm yDpnqmf jt' \
             ' cfuufs boui dbufe/dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf uibo otf/ef uzSfbebcjmj vout/dp' \
             ' djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ipvhiBmu zqsbdujdbmju fbutc uz/qvsj Fsspst' \
             ' tipvme wfsof qbtt foumz/tjm omfttV mjdjumzfyq odfe/tjmf Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq ' \
             'up ftt/hv Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ Bmuipvhi uibu bzx bzn puo' \
             ' cf wjpvtpc bu jstug ttvomf sfzpv( i/Evud xOp tj scfuuf ibou /ofwfs uipvhiBm fsofw jt fopgu cfuufs boui ' \
             'iu++sjh x/op gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /jefb Jg fui foubujpojnqmfn jt fbtz up ' \
             'bjo-fyqm ju znb cf b hppe jefb/ bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip'.lower()
simb_list = '!@#$%^&*(_)-><?.,;:/+"'
eng_alphabet = list('abcdefghijklmnopqrstuvwxyz')


itr = 1
user_output = []
user_input_mass = user_input.split(' ')
for index, word in enumerate(user_input_mass):
    new_word = []
    for letter in word:
        # eng_alphabet.index(letter)
        if letter in simb_list:
            new_word.append(letter)
            continue
        letter_index = eng_alphabet.index(letter)
        if letter_index - itr < 0:
            letter_index += 26
        new_letter = eng_alphabet[letter_index - itr]
        new_word.append(new_letter)
    user_output.append(''.join(new_word))
    if index % 8 == 0 :
        user_output.append('\n')

print(' '.join(user_output))
