"""Precomments_keybinding

Revision ID: 367f9e9f7f12
Revises: a0d873d038a9
Create Date: 2022-03-08 14:28:21.558121

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '367f9e9f7f12'
down_revision = 'a0d873d038a9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('precomment', schema=None) as batch_op:
        batch_op.add_column(sa.Column('keybinding', sa.String(length=3), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('precomment', schema=None) as batch_op:
        batch_op.drop_column('keybinding')

    # ### end Alembic commands ###