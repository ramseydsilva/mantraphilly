
def get_file_path(extension=''):
    def f(instance, filename):
        if "." in filename:
            return '{0}/{1}/{2}'.format(instance._meta.model_name, instance.id, filename).lower()
        else:
            return '{0}/{1}/{2}.{3}'.format(instance._meta.model_name, instance.id, filename, extension).lower()
    return f
