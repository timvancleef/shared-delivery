"""empty message

Revision ID: 00f6de819d35
Revises: 
Create Date: 2020-03-24 08:48:38.817870

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '00f6de819d35'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('modified', sa.DateTime(), nullable=False),
    sa.Column('slug', sa.String(length=255), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('logo', sa.Enum('jpg', 'png'), nullable=True),
    sa.Column('picture', sa.Enum('jpg', 'png'), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_charset='utf8',
    mysql_collate='utf8_unicode_ci'
    )
    op.create_table('object_history',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('modified', sa.DateTime(), nullable=False),
    sa.Column('object_id', sa.Integer(), nullable=True),
    sa.Column('type', sa.String(length=255), nullable=True),
    sa.Column('data', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_charset='utf8',
    mysql_collate='utf8_unicode_ci'
    )
    op.create_index(op.f('ix_object_history_type'), 'object_history', ['type'], unique=False)
    op.create_table('option',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('modified', sa.DateTime(), nullable=False),
    sa.Column('key', sa.String(length=128), nullable=True),
    sa.Column('type', sa.Enum('string', 'date', 'datetime', 'integer', 'decimal', 'dict', 'list'), nullable=True),
    sa.Column('value', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_charset='utf8',
    mysql_collate='utf8_unicode_ci'
    )
    op.create_index(op.f('ix_option_key'), 'option', ['key'], unique=False)
    op.create_table('region',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('modified', sa.DateTime(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('website', sa.String(length=255), nullable=True),
    sa.Column('area', sa.Text(), nullable=True),
    sa.Column('lat', sa.Numeric(precision=8, scale=6), nullable=True),
    sa.Column('lon', sa.Numeric(precision=9, scale=6), nullable=True),
    sa.Column('logo', sa.Enum('jpg', 'png'), nullable=True),
    sa.Column('picture', sa.Enum('jpg', 'png'), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_charset='utf8',
    mysql_collate='utf8_unicode_ci'
    )
    op.create_table('store',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('modified', sa.DateTime(), nullable=False),
    sa.Column('region_id', sa.Integer(), nullable=True),
    sa.Column('osm_id', sa.BigInteger(), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('firstname', sa.String(length=255), nullable=True),
    sa.Column('lastname', sa.String(length=255), nullable=True),
    sa.Column('company', sa.String(length=255), nullable=True),
    sa.Column('address', sa.String(length=255), nullable=True),
    sa.Column('postalcode', sa.String(length=255), nullable=True),
    sa.Column('locality', sa.String(length=255), nullable=True),
    sa.Column('country', sa.String(length=2), nullable=True),
    sa.Column('lat', sa.Numeric(precision=8, scale=6), nullable=True),
    sa.Column('lon', sa.Numeric(precision=9, scale=6), nullable=True),
    sa.Column('website', sa.String(length=255), nullable=True),
    sa.Column('website_crowdfunding', sa.String(length=255), nullable=True),
    sa.Column('website_coupon', sa.String(length=255), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('phone', sa.String(length=255), nullable=True),
    sa.Column('mobile', sa.String(length=255), nullable=True),
    sa.Column('fax', sa.String(length=255), nullable=True),
    sa.Column('revisited_government', sa.DateTime(), nullable=True),
    sa.Column('revisited_store', sa.DateTime(), nullable=True),
    sa.Column('revisited_user', sa.DateTime(), nullable=True),
    sa.Column('delivery', sa.Boolean(), nullable=True),
    sa.Column('pickup', sa.Boolean(), nullable=True),
    sa.Column('licence', sa.String(length=255), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('brand', sa.String(length=255), nullable=True),
    sa.Column('wheelchair', sa.String(length=255), nullable=True),
    sa.Column('logo', sa.Enum('jpg', 'png'), nullable=True),
    sa.Column('picture', sa.Enum('jpg', 'png'), nullable=True),
    sa.ForeignKeyConstraint(['region_id'], ['region.id'], ),
    sa.PrimaryKeyConstraint('id'),
    mysql_charset='utf8',
    mysql_collate='utf8_unicode_ci'
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('modified', sa.DateTime(), nullable=False),
    sa.Column('region_id', sa.Integer(), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('login_datetime', sa.DateTime(), nullable=True),
    sa.Column('last_login_datetime', sa.DateTime(), nullable=True),
    sa.Column('login_ip', sa.String(length=64), nullable=True),
    sa.Column('last_login_ip', sa.String(length=64), nullable=True),
    sa.Column('failed_login_count', sa.Integer(), nullable=True),
    sa.Column('last_failed_login_count', sa.Integer(), nullable=True),
    sa.Column('firstname', sa.String(length=255), nullable=True),
    sa.Column('lastname', sa.String(length=255), nullable=True),
    sa.Column('company', sa.String(length=255), nullable=True),
    sa.Column('address', sa.String(length=255), nullable=True),
    sa.Column('postalcode', sa.String(length=255), nullable=True),
    sa.Column('locality', sa.String(length=255), nullable=True),
    sa.Column('country', sa.String(length=2), nullable=True),
    sa.Column('language', sa.Enum('de', 'en'), nullable=True),
    sa.Column('phone', sa.String(length=255), nullable=True),
    sa.Column('mobile', sa.String(length=255), nullable=True),
    sa.Column('capabilities', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['region_id'], ['region.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    mysql_charset='utf8',
    mysql_collate='utf8_unicode_ci'
    )
    op.create_table('opening_time',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('modified', sa.DateTime(), nullable=False),
    sa.Column('store_id', sa.Integer(), nullable=True),
    sa.Column('type', sa.Enum('all', 'delivery', 'counter', 'pickup'), nullable=True),
    sa.Column('weekday', sa.Integer(), nullable=True),
    sa.Column('open', sa.Integer(), nullable=True),
    sa.Column('close', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['store_id'], ['store.id'], ),
    sa.PrimaryKeyConstraint('id'),
    mysql_charset='utf8',
    mysql_collate='utf8_unicode_ci'
    )
    op.create_table('store_category',
    sa.Column('store_id', sa.Integer(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.ForeignKeyConstraint(['store_id'], ['store.id'], )
    )
    op.create_table('tag',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('modified', sa.DateTime(), nullable=False),
    sa.Column('store_id', sa.Integer(), nullable=True),
    sa.Column('type', sa.Enum('offer', 'help'), nullable=True),
    sa.Column('slug', sa.String(length=255), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['store_id'], ['store.id'], ),
    sa.PrimaryKeyConstraint('id'),
    mysql_charset='utf8',
    mysql_collate='utf8_unicode_ci'
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tag')
    op.drop_table('store_category')
    op.drop_table('opening_time')
    op.drop_table('user')
    op.drop_table('store')
    op.drop_table('region')
    op.drop_index(op.f('ix_option_key'), table_name='option')
    op.drop_table('option')
    op.drop_index(op.f('ix_object_history_type'), table_name='object_history')
    op.drop_table('object_history')
    op.drop_table('category')
    # ### end Alembic commands ###