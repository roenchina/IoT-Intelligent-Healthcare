"""empty message

Revision ID: 922f6ce04f49
Revises: 488561e8eae2
Create Date: 2021-06-27 18:54:35.718937

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '922f6ce04f49'
down_revision = '488561e8eae2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('money', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'money')
    # ### end Alembic commands ###
