"""inupdated the pitches table.

Revision ID: 716029d0749c
Revises: b67f74365ac0
Create Date: 2018-11-21 18:17:26.534120

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '716029d0749c'
down_revision = 'b67f74365ac0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pitches', 'password_hash')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('password_hash', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
