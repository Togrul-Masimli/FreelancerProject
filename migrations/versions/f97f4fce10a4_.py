"""empty message

Revision ID: f97f4fce10a4
Revises: 38e19930c9a5
Create Date: 2021-06-18 18:35:19.260046

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f97f4fce10a4'
down_revision = '38e19930c9a5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('privacy',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('user_info')
    op.add_column('user', sa.Column('about_user', sa.Text(), nullable=True))
    op.add_column('user', sa.Column('education', sa.Text(), nullable=True))
    op.add_column('user', sa.Column('speciality', sa.String(length=20), nullable=True))
    op.add_column('user', sa.Column('location', sa.String(length=20), nullable=True))
    op.add_column('user', sa.Column('age', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('experience', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'experience')
    op.drop_column('user', 'age')
    op.drop_column('user', 'location')
    op.drop_column('user', 'speciality')
    op.drop_column('user', 'education')
    op.drop_column('user', 'about_user')
    op.create_table('user_info',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('about_user', sa.TEXT(), nullable=True),
    sa.Column('education', sa.TEXT(), nullable=True),
    sa.Column('speciality', sa.VARCHAR(length=20), nullable=True),
    sa.Column('location', sa.VARCHAR(length=20), nullable=True),
    sa.Column('age', sa.INTEGER(), nullable=True),
    sa.Column('experience', sa.INTEGER(), nullable=True),
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('privacy')
    # ### end Alembic commands ###
