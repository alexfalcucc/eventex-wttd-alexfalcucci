# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Speaker'
        db.create_table(u'core_speaker', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'core', ['Speaker'])

        # Adding model 'Contact'
        db.create_table(u'core_contact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('speaker', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Speaker'])),
            ('kind', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'core', ['Contact'])

        # Adding model 'Talk'
        db.create_table(u'core_talk', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('start_time', self.gf('django.db.models.fields.TimeField')(blank=True)),
        ))
        db.send_create_signal(u'core', ['Talk'])

        # Adding M2M table for field speakers on 'Talk'
        m2m_table_name = db.shorten_name(u'core_talk_speakers')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('talk', models.ForeignKey(orm[u'core.talk'], null=False)),
            ('speaker', models.ForeignKey(orm[u'core.speaker'], null=False))
        ))
        db.create_unique(m2m_table_name, ['talk_id', 'speaker_id'])

        # Adding model 'Course'
        db.create_table(u'core_course', (
            (u'talk_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.Talk'], unique=True, primary_key=True)),
            ('slots', self.gf('django.db.models.fields.IntegerField')()),
            ('notes', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'core', ['Course'])

        # Adding model 'Media'
        db.create_table(u'core_media', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('talk', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Talk'])),
            ('kind', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('media_id', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'core', ['Media'])


    def backwards(self, orm):
        # Deleting model 'Speaker'
        db.delete_table(u'core_speaker')

        # Deleting model 'Contact'
        db.delete_table(u'core_contact')

        # Deleting model 'Talk'
        db.delete_table(u'core_talk')

        # Removing M2M table for field speakers on 'Talk'
        db.delete_table(db.shorten_name(u'core_talk_speakers'))

        # Deleting model 'Course'
        db.delete_table(u'core_course')

        # Deleting model 'Media'
        db.delete_table(u'core_media')


    models = {
        u'core.contact': {
            'Meta': {'object_name': 'Contact'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'speaker': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Speaker']"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'core.course': {
            'Meta': {'object_name': 'Course', '_ormbases': [u'core.Talk']},
            'notes': ('django.db.models.fields.TextField', [], {}),
            'slots': ('django.db.models.fields.IntegerField', [], {}),
            u'talk_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Talk']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'core.media': {
            'Meta': {'object_name': 'Media'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'media_id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'talk': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Talk']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'core.speaker': {
            'Meta': {'object_name': 'Speaker'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'core.talk': {
            'Meta': {'object_name': 'Talk'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'speakers': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.Speaker']", 'symmetrical': 'False'}),
            'start_time': ('django.db.models.fields.TimeField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['core']