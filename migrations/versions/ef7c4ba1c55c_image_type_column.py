"""Image type column

Revision ID: ef7c4ba1c55c
Revises: bca0f7c62230
Create Date: 2021-05-20 14:50:38.425141

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ef7c4ba1c55c'
down_revision = 'bca0f7c62230'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('image', sa.Column('imgtype', sa.String(length=16), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('image', 'imgtype')
    # ### end Alembic commands ###
