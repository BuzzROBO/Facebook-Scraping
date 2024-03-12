from waitress import serve
import falcon
from falcon_cors import CORS
import os



cors = CORS(allow_all_origins=True, allow_all_headers=True, allow_credentials_all_origins=True, allow_all_methods=True)



class user:
    _required_params = ["file_name"]
    _dot_string = '-----'
    dir = os.path.dirname(__file__)

    def _handleQuery(self, provided_params):
        _required_params = self._required_params
        # Checking whether we are getting all the required parameters. Incomplete parameters will result in an error
        all_params_provided = all([False if param not in provided_params else True for param in _required_params])
        # If we are not getting all the parameters, we gracefully exit with an error statement
        if not all_params_provided:
            return {'Error': 'Missing Parameter. Make Sure all parameters are present. Valid parameters are '
                             '{0}'.format(', '.join(_required_params))}
        name = provided_params['file_name'] if provided_params['file_name'] else None
        print(name)
        try:
            file = open(name, "r")
            content = file.read()
            print(content)
            file.close()
            return {
                    "count": content,
                    }
        except:
            return {
                    "count": 0,
                    }
                        

    def on_get(self, req, resp):
        params = req.params
        resp.media = self._handleQuery(params)

    def on_post(self, req, resp):
        params = req.media
        resp.media = self._handleQuery(params)


if __name__ == '__main__':
    api = falcon.API(middleware=[cors.middleware])
    api.add_route('/user_count', user())
    serve(api, host='localhost', port=8058)
