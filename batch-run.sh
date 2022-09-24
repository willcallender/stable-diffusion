readarray -t lines < <(sort -u lyrics.txt | grep .)

for line in "${lines[@]}"
do
python3 optimizedSD/optimized_txt2img.py --n_samples 50 --n_iter 2 --prompt "$line, art, symbolism, metaphor, melancholy"
done
