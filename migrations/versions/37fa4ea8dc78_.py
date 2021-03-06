"""empty message

Revision ID: 37fa4ea8dc78
Revises: 3de8be8e1671
Create Date: 2015-11-03 11:26:12.662594

"""

# revision identifiers, used by Alembic.
revision = '37fa4ea8dc78'
down_revision = '3de8be8e1671'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('downvoted', 'timestamp')
    op.drop_column('upvoted', 'timestamp')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('upvoted', sa.Column('timestamp', sa.DATETIME(), nullable=True))
    op.add_column('downvoted', sa.Column('timestamp', sa.DATETIME(), nullable=True))
    ### end Alembic commands ###
