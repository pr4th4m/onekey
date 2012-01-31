# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Test.first_name'
        db.add_column('services_test', 'first_name', self.gf('django.db.models.fields.CharField')(default='', max_length=20), keep_default=False)

        # Adding field 'Test.last_name'
        db.add_column('services_test', 'last_name', self.gf('django.db.models.fields.CharField')(default='', max_length=20), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Test.first_name'
        db.delete_column('services_test', 'first_name')

        # Deleting field 'Test.last_name'
        db.delete_column('services_test', 'last_name')


    models = {
        'services.test': {
            'Meta': {'object_name': 'Test'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'test_field': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['services']
