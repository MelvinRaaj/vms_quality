while read line; do
  package="$(echo $line | tr -d '[:space:]')"
  if [ ! -z "$package" ]; then
    pip uninstall -y $package
  fi
done < requirements.txt