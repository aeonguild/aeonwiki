cd chart-maker/
python3 update.py
cd ..
rm -r docs/network-info/charts/*/
cp -r chart-maker/charts/* docs/network-info/charts/

#./node-scraper/moneriote.sh
#mv node-scraper/open-nodes.md docs/network-info/

python3 -m mkdocs build
rm -r /var/www/aeon.wiki/html/*
cp -r site/* /var/www/aeon.wiki/html/
sudo service nginx restart
