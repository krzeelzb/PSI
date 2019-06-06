# PSI
Project for Artifitial Inteligence Course

## Opis wygenerowanych kolumn w preprocessingu

*id* - id osoby, biorącej udział w badaniach (różne dla różnych plików)
*sound_number* - id słyszanego dźwięku
*sound_valence_mean* - średnia wartościowość dźwięku na podstawie odpowiedzi 10 tys ankietowanych
*sound_arousal_mean* - jw tylko z podnieceniem
*is_sound_positive* - czy dźwięk pozytywny na podstawie zmiennej pXsX z oryginalnego pliku (np p+s- oznacza pozytywny obrazek, negatywny dźwięk)
*is_sound_obscene* - czy dźwięk jest nieprzyzwoity, na podstawie opisu dźwięku (jeśli zaczyna się od erotic albo nude to jest nieprzyzwoity)
TO SAMO DLA PICTURES
*not_processed_answer* - odpowiedź badanej osoby w skali ciągłej -1;1 po lewej wartość wartościowości, po prawej podniecalności
*answer_valence* - odpowiedź badanej osoby po przeskalowaniu od 1 do 9 
*answer_arousal* - jak wyżej tylko z podnieceniem
