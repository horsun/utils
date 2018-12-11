from Lyonline.settings import error_logger


class ExceptionLoggingMiddleware(object):
    def process_exception(self, request, exception):
        import traceback
        error_logger.error(traceback.format_exc())
