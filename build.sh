cd chart_maker/
python3 update.py
cd ..
rm -r docs/network-info/charts/*/
cp -r chart_maker/charts/* docs/network-info/charts/

./node_scraper/moneriote.sh
mv node_scraper/open-nodes.md docs/network-info/

python3 -m mkdocs build
rm -r /var/www/aeon.wiki/html/*
cp -r site/* /var/www/aeon.wiki/html/
sudo service nginx restart
