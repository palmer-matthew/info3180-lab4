from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileRequired, FileField

class UploadForm(FlaskForm):
    
    file = FileField('Photo Upload', validators= [FileRequired(), FileAllowed(['jpg','png','Images only!'])])