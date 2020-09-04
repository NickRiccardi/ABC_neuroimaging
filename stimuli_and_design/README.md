# Stimuli and Design

This folder contains stimuli used in the ABC@UofSC project for language task fMRI and EEG. There were two tasks: passage listening and word reading. Pictures and audio files can be found at: https://osf.io/buk34/

## Folders and files for 'fMRI_passage' task

- listening_texts.csv
    - Folder with materials for the listening task.

- Story_Questions.docx
    - Questions asked at the end of the passage with choices.

- texts
    - Text files of the narratives.

- timestamps
    - Onset of every word and every sentence in milliseconds since the beginning of the passage. Contains word, onset time, and offset time columns. @ indicates start of a new sentence.

## Folders and files for 'fMRI_fam' task

- master_word

Listing of each word, nonword, and picture used in the task. Various categories are marked using a coding system, also used in the Eprime experiment scripts, in order to make analysis convenient.

    1. master_word_lemmatized_list.csv
        - Main word (and picture) list with associated codes and many psycholinguistic properties taken from ELP and other sources.
    2. master_word_Codes_Organize.csv
        - A summary of all the various big and small categories built into the stimuli, and their codes.
    3. master_word_Nonwords.csv
        - Listing and psycholinguistic properties of the nonwords.

- pic_stimuli.csv
    - Information about the picture stimuli.

- eprime_scripts
    - Sample experimental scripts used to present stimuli.

## Listening Task ('fMRI_passage')

![listening_task](https://user-images.githubusercontent.com/64374486/80320249-5e70d400-87e3-11ea-969c-e7ac4af7fe7c.png)

-	This task was identical for fMRI and EEG, and was 8 minutes long.
-	Subjects heard an audio recording of a narrative for 6 minutes. 
-	Subjects answered 4 or 5 multiple choice questions after the passage, as a test for comprehension.
-	There were 23 different passages, each read by a male and a female speaker. Thus, there were 46 total recordings. There were multiple male and multiple female speakers.
-	Each subject got one of the 46 recordings for fMRI, and one for EEG. Both were selected at random and not paired in any way.
-	Over 40,400 words and 4.6 hours of recording over 46 passages
-	Forty recordings were made in a soundproof booth by multiple speakers. Six were created by Google Cloud text-to-speech deep learning speech synthesizer.
-	Each recording had a 50-second foreign language passage played before and after it. There were eight such passages, four Hindi and four Thai. Each had two male and two female speakers. One Hindi and one Thai passage was played for each subject. Gender was matched to that of the English passage (e.g., if a subject got a female English passage, they would get a female Hindi and a female Thai passage).
-	The passages were selected to increase the variability of texts, in multiple dimensions, in order to create a rich stimulus set that would allow examination of many different questions. Some example manipulations that are included are:
    - Overall difficulty: ‘Easy’ 5th-6th grade level stories that have mainly high frequency words and simpler sentences, to more ‘advanced’ texts with more complex content.
    - Affect: A particularly ‘happy’ and a particularly ‘sad’ story, with levels in between. Single sentences with five types of emotions.
    - Syntactic structure: Five stories that contain more complex and noncanonical sentence structures (which tend to have very low frequency in ‘real world’ texts) while being comprehensible. Taken from the Natural Stories Corpus database.
    - Genre: Both ‘narrative’ (story-like) and ‘expository’ (convey factual information) style of passages, including fiction and nonfiction passages.
    - Reference: For two stories, two versions were created. One uses proper names repeatedly (‘Lucy did this’), while the other uses pronouns (‘She did this’). Allows examination of   the ‘repeated name penalty’ and reference tracking.
    - Discourse length: Some narratives are comprised of multiple unconnected shorter stories of varying length, and one contains single (unconnected) sentences. Majority are a single long narrative. Allows examination of building of discourse structure over time.
    - Nonliteral language: Some passages contain metaphoric and ironic content.
    - Gender and voice: Availably of the same content in male and female voices, and inclusion of multiple male and female voices allows possible examination of (or at least a control for) effects of gender and voice.
    - Language laterality: Foreign language passages were included as controls to allow estimation of general language areas and language laterality. 
    - Lexical categories: The sheer length and variety of texts allows examination of many different lexical properties, including psycholinguistic variables (frequency, concreteness, regularity, etc.), semantic classes (living, nonliving, tools, actions, numbers, etc.) and all major grammatical classes.
    - Sublexical properties: By coding sublexical feature of the stimuli such as particular phonemes, biphone or bigram frequency, phonological neighborhood, etc., analysis of these properties is possible.
-	A timestamp file marking the onset of every word and every sentence was created for each of the recordings. This was originally generated by Google Cloud speech-to-text deep learning speech recognition system, with 100 ms resolution. Each timestamp file was manually examined and corrected. This file can be used to generate timing files for fMRI and EEG analysis at the word or sentence level.

## Reading Task ('fMRI_fam')

![reading_task](https://user-images.githubusercontent.com/64374486/80320360-fcfd3500-87e3-11ea-95fa-e717c05018cc.png)

-	Stimulus is shown on the screen for 2 sec, followed by variable jitter
-	Participant makes a familiarity judgment by pressing one of three buttons: highly familiar, less familiar, or unfamiliar.
-	Total length of scan 8 min; 95 stimuli per subject.
-	A small number of nonword and picture stimuli are ensured for each subject.
-	As in the listening task, stimuli were selected to maximize variation to create a rich dataset and allow examination of many different questions.
-	Stimuli for fMRI and EEG were selected randomly, and not paired in any way.
-	1524 words, 110 nonwords, 180 pictures
    - Words: Nouns (692), verbs (452), adjectives (94), adverbs (58), numbers/digits (40), closed class words (88), and proper names (100).
    - Nonwords: Pronounceable pseudowords (60), unpronounceable nonwords (25), consonant strings (25). 
    - Pictures: Objects (35), actions (30), emotional faces (30), famous people and places (30), scenes (30), scrambled (25).
-	Special effort was made to increase representation of words other than concrete nouns, which is the most commonly studied category. Verbs and other grammatical classes, and abstract words have a stronger representation in this set, as those are likely to yield more novel results be useful for future studies. Each of these categories have many subcategories, detailed in the file mentioned below. Examples of some of the built-in variables and manipulations are:
    - Transitive (30) and intransitive (30) verbs closely matched 
    - Event nouns (80) and object nouns (80) closely matched 
    - Systematic variation in frequency
    - Systematic variation in concreteness/imageability
    - Systematic variation in spelling-sound consistency (words with high (100) and low (100) consistency, closely matched)  
    - Emotion words with 2x2 positive/negative valence and high/low arousal (40+)
    - Unique entities 2x2 famous/nonfamous, people/places (100)
    - Many abstract words including superordinate concrete and abstract category terms
    - Many semantic subcategories of nouns, verbs, adjectives, adverbs, pictures
    - Systematic variation in the orthographic neighborhood size (Orthographic Levenshtein Distance or OLD20) for pseudowords, so that some have many real word neighbors and some have few
    - Some words from the listening task (especially those that occur multiple times in passages) were included here to increase the overlap between the two tasks. In all, 525 lemmas are common between the two tasks. Allows comparison of words presented in isolation vs. those occurring in naturalistic context.
