from flask_wtf import FlaskForm
from wtforms import SubmitField, FileField
from wtforms.validators import DataRequired

class Model_1(FlaskForm):

    data = FileField(validators=[DataRequired()])
    Submit = SubmitField('Run Model')

    
    
    
