for letter in {b..z} ; do
  echo $letter
  cp char_a.gcode char_$letter.gcode
  #rm char_$letter.gcode
done
