export BRANCH="speedrun"
export FILENAME="speedrun.sh"
export CONTENT=""
git clone https://github.com/janine9vn/Git-GitHub-Bootcamp.git
cd Git-GitHub-Bootcamp
git checkout -b $BRANCH
echo $CONTENT >> add_file_here/$FILENAME
git add .
git commit -m "Hi"
git push origin $BRANCH
gh pr create -a @me -B main -H $BRANCH -t Hi -b ""
gh pr merge --auto -m -d
cd -
rm -rf Git-GitHub-Bootcamp
