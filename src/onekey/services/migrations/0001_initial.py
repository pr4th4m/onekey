# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Test'
        db.create_table('services_test', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('test_field', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('services', ['Test'])


    def backwards(self, orm):
        
        # Deleting model 'Test'
        db.delete_table('services_test')


    models = {
        'services.test': {
            'Meta': {'object_name': 'Test'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'test_field': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['services']
