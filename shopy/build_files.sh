

pip install -r requirements.txt
python3.9 manage.py collectstatic --noinput
mkdir -p staticfiles/
cp -r static/ staticfiles/
cp -r media/ staticfiles/
