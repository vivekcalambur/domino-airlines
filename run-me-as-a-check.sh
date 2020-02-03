python get-runtime-info.py

echo -e "\nWorking Directory: "
pwd

echo -e "\nDirectory Tree\n--------------"
find $HOME -maxdepth 2 -type d | sed -e "s/[^-][^\/]*\//  |/g" -e "s/|\([^ ]\)/|-\1/"
