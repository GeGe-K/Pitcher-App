"""added the classes comment and pitch.

Revision ID: 9d0c25ad18b3
Revises: ab0e2a2f42c6
Create Date: 2018-11-19 17:10:30.207222

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9d0c25ad18b3'
down_revision = 'ab0e2a2f42c6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pitches',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=True),
    sa.Column('content', sa.String(length=255), nullable=True),
    sa.Column('category', sa.String(), nullable=True),
    sa.Column('password_hash', sa.String(length=255), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('date', sa.String(length=255), nullable=True),
    sa.Column('time', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pitch_id', sa.Integer(), nullable=True),
    sa.Column('comment', sa.String(length=255), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('date', sa.String(length=255), nullable=True),
    sa.Column('time', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['pitch_id'], ['pitches.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comments')
    op.drop_table('pitches')
    # ### end Alembic commands ###
