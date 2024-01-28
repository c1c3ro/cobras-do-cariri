# PARAMS=('-m 6 -q 70 -mt -af -progress')

# if [ $# -ne 0 ]; then
# 	PARAMS=$@;
# fi

# cd $(pwd)

# shopt -s nullglob nocaseglob extglob

# for FILE in *.@(jpg|jpeg|tif|tiff|png); do 
#     cwebp $PARAMS "$FILE" -o "${FILE%.*}".webp;
#     rm $FILE;
# done

#!/bin/zsh

# Define the image types to search for
image_types=("*.jpeg" "*.jpg" "*.tiff" "*.tif" "*.png")

# Iterate over each image type
for type in "${image_types[@]}"; do
  # Find files of the specified image type
  find . -type f -iname "$type" | while read -r IMAGE; do
    # Get the filename without extension
   filename_without_extension=${IMAGE%.*}
   
    # Convert the image to WebP format
    cwebp "$IMAGE" -o "${filename_without_extension}.webp"

    echo "Converted $IMAGE to ${filename_without_extension}.webp"

     rm "$IMAGE";
  done
done

echo "Conversion complete."