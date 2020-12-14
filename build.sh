cd charts/
python3 exec.py
cd ..
rm -r docs/network-info/charts/*/
cp -r charts/charts/* docs/network-info/charts/

#./node-scraper/moneriote.sh
#mv node-scraper/open-nodes.md docs/network-info/

python3 -m mkdocs build
rm -r /var/www/aeon.wiki/html/*
cp -r site/* /var/www/aeon.wiki/html/
sudo service nginx restart
