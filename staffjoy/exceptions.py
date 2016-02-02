class UnauthorizedException(Exception):
    def __init__(self, code=401, response={}):

        self.code = code
        # We envelope error messages like this
        self.message = response.get("message", "Unknown Error")
        super(UnauthorizedException, self).__init__()

    def __str__(self):
        return '\n Status: %s \n Reason: %s \n Error Message: %s\n' % (
            self.code, self.reason, self.error_message)


class NotFoundException(Exception):
    def __init__(self, code=404, response={}):

        self.code = code
        # We envelope error messages like this
        self.message = response.get("message", "Unknown Error")
        super(UnauthorizedException, self).__init__()

    def __str__(self):
        return '\n Status: %s \n Reason: %s \n Error Message: %s\n' % (
            self.code, self.reason, self.error_message)


class BadRequestException(Exception):
    def __init__(self, code=401, response={}):

        self.code = code
        # We envelope error messages like this
        self.message = response.get("message", "Unknown Error")
        super(UnauthorizedException, self).__init__()

    def __str__(self):
        return '\n Status: %s \n Reason: %s \n Error Message: %s\n' % (
            self.code, self.reason, self.error_message)