# LOREM IPSUM

tekst = '''
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
    Etiam eu purus at neque varius mattis fermentum vel erat. 
    Nunc in orci in risus ultricies mollis id at dolor. 
    Pellentesque habitant morbi tristique senectus et netus et 
    malesuada fames ac turpis egestas. Nulla facilisi. 
    Vestibulum vitae tellus laoreet massa semper tempor. 
    Integer in magna sit amet nisl tincidunt tincidunt 
    quis et eros. Nullam diam enim, finibus eget leo at, 
    mattis eleifend odio. Phasellus sit amet facilisis est, 
    in porttitor nulla. Quisque feugiat non sapien ac blandit. 
    Aliquam tincidunt, urna nec pretium aliquam, lorem lorem 
    venenatis libero, fermentum ullamcorper urna orci eget leo. 
    Proin lacinia, purus id varius ultricies, ligula lacus 
    vehicula odio, a luctus velit purus a elit. Vivamus laoreet 
    metus in volutpat ultrices. Proin laoreet est eget ex sodales, 
    ac blandit nulla lacinia. Mauris elementum blandit lacinia. 
    Aenean id mi ac nunc porta suscipit sed quis turpis. Curabitur 
    nunc tellus, lobortis ac pharetra id, euismod a elit. Quisque 
    vulputate, erat eu cursus ullamcorper, ligula dui dignissim 
    lacus, sed finibus diam libero quis felis.
    Morbi vitae aliquet elit. Cras maximus mauris sit amet augue 
    porta, sed placerat metus efficitur. Donec purus neque, aliquet
     elementum ex eu, pellentesque efficitur metus. Nulla ultrices, 
     justo id faucibus tincidunt, leo nibh finibus odio, et dictum 
     quam risus vulputate orci. Quisque congue dui nisi, tincidunt 
     pellentesque odio tristique sit amet. Nam vel sagittis nibh. 
     Sed pellentesque in turpis in pretium. Quisque velit ligula, 
     rutrum ut molestie nec, pharetra non ipsum. Nulla volutpat erat
      ac turpis posuere placerat. Donec sit amet justo erat. Maecenas 
      interdum lacus at erat maximus, ut scelerisque dui pretium. 
      Mauris rhoncus tellus diam, vel rutrum orci hendrerit et. 
      Fusce mollis ornare tortor, a venenatis velit ultricies ut.
      Vivamus ipsum augue, posuere in eros vel, faucibus tempor nunc. 
      Phasellus in elit quis nisl varius pharetra. Integer at orci 
      scelerisque, accumsan mauris et, egestas dolor. Donec dapibus
       non dolor id scelerisque. Cras eu leo auctor, blandit orci quis,
        iaculis quam. Maecenas congue efficitur leo at eleifend. 
        Vivamus feugiat enim ut nisl consectetur, at porttitor lorem eleifend. 
        Sed cursus blandit mollis. Nunc volutpat egestas lacus a egestas.
         Nunc sed sapien sapien. Phasellus ultricies velit nec arcu commodo, 
         ac congue velit interdum. Morbi nec enim quis est blandit volutpat.
          Nulla non placerat nulla. Nunc ornare eleifend nunc eget laoreet.
           Aenean aliquam nibh nec feugiat sodales.
    Suspendisse efficitur diam eros, a sodales tortor placerat at. 
    Class aptent taciti sociosqu ad litora torquent per conubia nostra, 
    per inceptos himenaeos. Donec commodo porttitor elit, vel pulvinar 
    purus viverra vitae. Suspendisse pellentesque vitae libero id volutpat. 
    Integer velit quam, ornare ac tellus sed, ullamcorper scelerisque elit.
     Integer et metus in enim pellentesque iaculis. Phasellus eget nulla 
     et dui porttitor accumsan vel ac orci. Duis sed eleifend nulla. 
     Vestibulum non sapien massa. Cras fringilla nibh sed iaculis pretium. 
     Quisque accumsan ac diam sed aliquam. Duis feugiat, mi vitae dapibus 
     blandit, diam ligula tristique nibh, sed sodales metus orci nec urna. 
     Etiam malesuada, magna in luctus rutrum, magna mauris eleifend tortor, 
     vel luctus sapien eros id magna. Nulla rutrum ex vitae finibus mattis.
'''
tekst = tekst.lower()
print(tekst)
word = 'lorem'
word_1 = 'ipsum'
counter = tekst.count(word)
counter_1 = tekst.count(word_1)

print(f'\nRiječ {word} se pojavljuje {counter} puta u tekstu.')

print(f'\nRiječ {word_1} se pojavljuje {counter_1} puta u tekstu.')

