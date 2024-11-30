from tornado.web import Application, RequestHandler
from tornado.routing import Rule, PathMatches
import gc
import streamlit as st


@st.cache_resource()
def setup_api_handler(uri, handler):
    print("Setup Tornado. Should be called only once")

    # Get instance of Tornado
    tornado_app = next(o for o in gc.get_referrers(Application) if o.__class__ is Application)

    # Setup custom handler
    tornado_app.wildcard_router.rules.insert(0, Rule(PathMatches(uri), handler))


class HelloHandler(RequestHandler):
  def get(self):
    self.write({'message': 'hello world'})


if __name__ == '__main__':

    setup_api_handler('/api/hello', HelloHandler)




# import streamlit as st

# import uvicorn
# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware

# app = FastAPI()

# app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

# @app.get('/')
# def root():
#     print('Hello World!')
#     return {'Hello': 'World'}


# @app.get('/ciao')
# def say_ciao():
#     print('ciaooo')
#     return {'ciao': 'ciao'}


# if __name__ == '__main__':

#     uvicorn.run(app, host='0.0.0.0', port=8000)
