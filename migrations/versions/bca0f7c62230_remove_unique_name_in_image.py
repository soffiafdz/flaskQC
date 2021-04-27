"""Remove unique name in Image

Revision ID: bca0f7c62230
Revises: a18b7593de7c
Create Date: 2021-04-04 22:21:29.316727

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bca0f7c62230'
down_revision = 'a18b7593de7c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_image_name', table_name='image')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_image_name', 'image', ['name'], unique=1)
    # ### end Alembic commands ###