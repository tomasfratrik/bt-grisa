# API endpoint for GRISA
Using `GRISA` as a submodule, this program creates an API with endpoints for it.
Implementation of `GRISA` can be found in the `grisa` folder

### Local dev
create virtual enviroment with `python3 -m venv venv`
activate it with `. venv/bin/activate`
install all requirements with `pip install -r requirements.txt`
run `python3 app.py`

### API Endpoints

`/ping` [GET]
- testing endpoing
- should get `pong`

`/grisa/upload` [POST]
- uploading image to GRISA

`/grisa/upload/url/<path:url>`[POST]
- uploading URL to GRISA

### Return format (JSON)
```
'similar_imgs': similar_img_json,
'source_imgs': source_img_json
```

- Where `similar_img_json` is a list of objects:
``` 
{ 
    'website': website name,
    'description': description,
    'imageurl': url link to image,
    'link': url link to ad listing,
    'position': position in which it was found,
}
```
Careful, the description is incomplete, containing sometimes only 5 words!

- Same for `source_img_json`, with addition of: 
```
'resolution': (x,y),
```

## Hosting
- hosted on Heroku
- URL: `https://bt-grisa-23ef74667d4f.herokuapp.com/`

### Heroku plugins
```
heroku-builds 0.0.29
heroku-fork 4.1.29
heroku-repo 1.0.14
```
### Heroku buildpacks
```
1. heroku-community/chrome-for-testing
2. heroku/python
```

