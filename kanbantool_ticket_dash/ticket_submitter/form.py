from flask_wtf import Form
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired


class TicketSubmitForm(Form):
      title        = StringField('Title', validators=[DataRequired()])
      submitted_by = StringField('Submitter', validators=[DataRequired()])
      due_date     = StringField('Due Date', validators=[DataRequired()])
      description  = TextAreaField('Description', validators=[DataRequired()])

