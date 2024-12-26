from pythonjsonlogger import jsonlogger

from django.utils import timezone


class AuthGroupJsonFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super(AuthGroupJsonFormatter, self).add_fields(log_record, record, message_dict)
        if not log_record.get('timestamp'):
            now = timezone.now().strftime('%d-%m-%Y %H:%M:%S')
            log_record['timestamp'] = now
        if log_record.get('level'):
            log_record['level'] = log_record['level'].upper()
        else:
            log_record['level'] = record.levelname

        log_record.pop("taskName", None)
        
        if hasattr(record, "username"):
            log_record["username"] = record.username
        else:
            log_record["username"] = None

formatter = AuthGroupJsonFormatter('%(timestamp)s %(level)s %(name)s %(message)s')
