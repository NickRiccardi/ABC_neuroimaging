ABC@UofSC fMRI/EEG stimuli
'listening/timestamps' folder
--------------------------
This folder contains texts file containing timestamps for each word (and sentence onset) in each of the recordings used
in the fMRI/EEG experiments. They represent time in seconds since the beginning of the passage, in 100 ms 
increments. (This is the best resolution avaialbe in the Google speech recognition system. It does not provide 
finer grained timestamps.) Timestamps were generated automatically by Google Cloud speech-to-text
speech recognition system. They were then examined and corrected manually. Many errors in speech
recognition were corrected. Several cases of alternative transcriptions (e.g., '50,000' and 
'fifty thousand'; 'upto' and 'up to') were also edited to make them identical between the
male and female versions. The intended use is to generate timing files for fMRI and EEG data analysis.

Each file has three columns, separated by a space. They represent the word, onset time of the word, 
and offset time of the word. Beginning of each sentence is marked with '@ @ @' for the three columns.

Both male and female versions of the recordings have identical words, except one case. Brandi_UserFriendly
has one more sentence at the end (12 extra appended words) compared to Jacob_UserFriendly.

The *_old.times.txt files are for the three recordings that have a mistake, but were used initially. They
were then replaced with the corrected version. The 'old' versions are included here because one or two subjects
initially may have been run with these files. They correspond to the .wav files
in the listening/recordings/removed/ folder. 
