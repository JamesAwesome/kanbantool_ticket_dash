from flask_wtf import Form
from wtforms import StringField, TextAreaField, DateField
from wtforms.validators import DataRequired, Optional, Regexp
import arrow

class TicketSubmitForm(Form):
      title        = StringField('Title', validators=[DataRequired()])
      submitted_by = StringField('Submitter', validators=[DataRequired()])
      due_date     = DateField('Due Date', format='%Y-%m-%d', validators=[Optional()], render_kw={"placeholder": "YYYY-MM-DD"})
      description  = TextAreaField('Description', validators=[DataRequired()])

      def validate_due_date(form, field):
          return arrow.get(field.data)
