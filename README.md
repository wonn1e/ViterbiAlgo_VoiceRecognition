# ViterbiAlgo_VoiceRecognition
Voice Recognizer with Viterbi Algorithm_implemented in Python

.:: Introduction ::. 
This is a continuous speech recognizer, specifically numbers. 
People have recorded their voice saying series of numbers from 0-9. 
Those records have been transformed into MFCC file and this recognizer is implemented using Viterbi algorithm.

.:: Specification of the files included ::.
The information needed to implement Viterbi algorithm such as language model probability, in this project, unigram.txt and bigram.txt;
how numbers are pronounciated in dictionary.txt; and the specification of each sound in hmm.txt.

There are two ways to say 0, which are 'oh' and 'zero'.
I have considered those two differently when finding the most probable word for each MFCC file.

tst directory is also included and whithin its lower level there are around 8000 MFCC files in txt format. 
The name of each txt file indicates the numbers that speaker is saying.
For instance, 44z5938 shows that person is saying "four four zero five nine three eight".

.:: How to run the program ::. 
You should be able to run the program with 'Viterbi.py' and since it's implemented in Python and the data in txt directory is enormous, it might take some time to finish running the whole program. If you wish to see the result more quickly, you should remove some files from txt directory.

.:: Results of the program ::.
As you finish running the program, you should be able to see the result in 'result.txt'.
In 'reference.txt' file, it shows what numbers are contained in each file and contrast to that, 
in 'recognized.txt', the most probable numbers recognized through the recognizer are shown.

You can get the confusion matrix using 'HResults.exe' file.
Using command prompt, change the current working directory to this project and type "HResults -p -I reference.txt dictionary.txt recognized.txt".

After testing all the files, the result has shown 99.72% of correctness in recognizing each word(number).
