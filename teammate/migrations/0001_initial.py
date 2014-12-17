# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Game'
        db.create_table(u'teammate_game', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('website', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('priority', self.gf('django.db.models.fields.IntegerField')(max_length=5)),
            ('post_count', self.gf('django.db.models.fields.IntegerField')(max_length=5)),
        ))
        db.send_create_signal(u'teammate', ['Game'])

        # Adding model 'CharacterAttr'
        db.create_table(u'teammate_characterattr', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('attr', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('value', self.gf('django.db.models.fields.IntegerField')(max_length=200)),
        ))
        db.send_create_signal(u'teammate', ['CharacterAttr'])

        # Adding model 'Attributes'
        db.create_table(u'teammate_attributes', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('game', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['teammate.Game'])),
            ('type', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'teammate', ['Attributes'])

        # Adding model 'Race'
        db.create_table(u'teammate_race', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('game', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['teammate.Game'])),
        ))
        db.send_create_signal(u'teammate', ['Race'])

        # Adding model 'Job'
        db.create_table(u'teammate_job', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('game', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['teammate.Game'])),
        ))
        db.send_create_signal(u'teammate', ['Job'])

        # Adding model 'Character'
        db.create_table(u'teammate_character', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('game', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['teammate.Game'])),
            ('race', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['teammate.Race'])),
            ('job', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['teammate.Job'])),
            ('desc', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'teammate', ['Character'])

        # Adding model 'Instance'
        db.create_table(u'teammate_instance', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('game', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['teammate.Game'])),
            ('priority', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=200)),
            ('post_count', self.gf('django.db.models.fields.IntegerField')(max_length=5)),
        ))
        db.send_create_signal(u'teammate', ['Instance'])

        # Adding model 'Skill'
        db.create_table(u'teammate_skill', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('game', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['teammate.Game'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'teammate', ['Skill'])

        # Adding model 'Topic'
        db.create_table(u'teammate_topic', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('game_name', self.gf('django.db.models.fields.related.ForeignKey')(related_name='topic_game', to=orm['teammate.Game'])),
            ('owner_name', self.gf('django.db.models.fields.related.ForeignKey')(related_name='topic_targets', to=orm['auth.User'])),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('Instance', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['teammate.Instance'])),
            ('quantity', self.gf('django.db.models.fields.IntegerField')(max_length=200)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('status', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('remark', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('chatroom', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'teammate', ['Topic'])

        # Adding model 'Requirement'
        db.create_table(u'teammate_requirement', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('games', self.gf('django.db.models.fields.related.ForeignKey')(related_name='topic_games', to=orm['teammate.Game'])),
            ('tank', self.gf('django.db.models.fields.IntegerField')(max_length=200)),
            ('healer', self.gf('django.db.models.fields.IntegerField')(max_length=200)),
            ('dpser', self.gf('django.db.models.fields.IntegerField')(max_length=200)),
            ('teammate', self.gf('django.db.models.fields.IntegerField')(max_length=200)),
            ('topics', self.gf('django.db.models.fields.related.ForeignKey')(related_name='topic_requirement', to=orm['teammate.Topic'])),
        ))
        db.send_create_signal(u'teammate', ['Requirement'])

        # Adding model 'Comment'
        db.create_table(u'teammate_comment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('topic_name', self.gf('django.db.models.fields.related.ForeignKey')(related_name='topic_name', to=orm['teammate.Topic'])),
            ('user_name', self.gf('django.db.models.fields.related.ForeignKey')(related_name='topic_users', to=orm['auth.User'])),
            ('message', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('created_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'teammate', ['Comment'])

        # Adding model 'Chatroom'
        db.create_table(u'teammate_chatroom', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='user_chatroom', to=orm['auth.User'])),
            ('peer_code', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
        ))
        db.send_create_signal(u'teammate', ['Chatroom'])

        # Adding model 'UserProfile'
        db.create_table(u'teammate_userprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(related_name='user_profile', unique=True, to=orm['auth.User'])),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('facebook_id', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('chatroom', self.gf('django.db.models.fields.related.ForeignKey')(related_name='userprofile_chatroom', null=True, to=orm['teammate.Chatroom'])),
            ('attitude', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
        ))
        db.send_create_signal(u'teammate', ['UserProfile'])

        # Adding model 'UserType'
        db.create_table(u'teammate_usertype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('type', self.gf('django.db.models.fields.IntegerField')(max_length=128)),
        ))
        db.send_create_signal(u'teammate', ['UserType'])

        # Adding model 'Personality'
        db.create_table(u'teammate_personality', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='from_user', to=orm['auth.User'])),
            ('by_user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='by_user', to=orm['auth.User'])),
            ('like', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['teammate.UserType'])),
        ))
        db.send_create_signal(u'teammate', ['Personality'])


    def backwards(self, orm):
        # Deleting model 'Game'
        db.delete_table(u'teammate_game')

        # Deleting model 'CharacterAttr'
        db.delete_table(u'teammate_characterattr')

        # Deleting model 'Attributes'
        db.delete_table(u'teammate_attributes')

        # Deleting model 'Race'
        db.delete_table(u'teammate_race')

        # Deleting model 'Job'
        db.delete_table(u'teammate_job')

        # Deleting model 'Character'
        db.delete_table(u'teammate_character')

        # Deleting model 'Instance'
        db.delete_table(u'teammate_instance')

        # Deleting model 'Skill'
        db.delete_table(u'teammate_skill')

        # Deleting model 'Topic'
        db.delete_table(u'teammate_topic')

        # Deleting model 'Requirement'
        db.delete_table(u'teammate_requirement')

        # Deleting model 'Comment'
        db.delete_table(u'teammate_comment')

        # Deleting model 'Chatroom'
        db.delete_table(u'teammate_chatroom')

        # Deleting model 'UserProfile'
        db.delete_table(u'teammate_userprofile')

        # Deleting model 'UserType'
        db.delete_table(u'teammate_usertype')

        # Deleting model 'Personality'
        db.delete_table(u'teammate_personality')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'teammate.attributes': {
            'Meta': {'object_name': 'Attributes'},
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['teammate.Game']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'type': ('django.db.models.fields.IntegerField', [], {})
        },
        u'teammate.character': {
            'Meta': {'object_name': 'Character'},
            'desc': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['teammate.Game']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['teammate.Job']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'race': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['teammate.Race']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'teammate.characterattr': {
            'Meta': {'object_name': 'CharacterAttr'},
            'attr': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'value': ('django.db.models.fields.IntegerField', [], {'max_length': '200'})
        },
        u'teammate.chatroom': {
            'Meta': {'object_name': 'Chatroom'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'peer_code': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user_chatroom'", 'to': u"orm['auth.User']"})
        },
        u'teammate.comment': {
            'Meta': {'object_name': 'Comment'},
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'topic_name': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'topic_name'", 'to': u"orm['teammate.Topic']"}),
            'user_name': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'topic_users'", 'to': u"orm['auth.User']"})
        },
        u'teammate.game': {
            'Meta': {'object_name': 'Game'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'post_count': ('django.db.models.fields.IntegerField', [], {'max_length': '5'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'max_length': '5'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'teammate.instance': {
            'Meta': {'object_name': 'Instance'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['teammate.Game']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'post_count': ('django.db.models.fields.IntegerField', [], {'max_length': '5'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '200'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'teammate.job': {
            'Meta': {'object_name': 'Job'},
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['teammate.Game']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'teammate.personality': {
            'Meta': {'object_name': 'Personality'},
            'by_user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'by_user'", 'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'like': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['teammate.UserType']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'from_user'", 'to': u"orm['auth.User']"})
        },
        u'teammate.race': {
            'Meta': {'object_name': 'Race'},
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['teammate.Game']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'teammate.requirement': {
            'Meta': {'object_name': 'Requirement'},
            'dpser': ('django.db.models.fields.IntegerField', [], {'max_length': '200'}),
            'games': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'topic_games'", 'to': u"orm['teammate.Game']"}),
            'healer': ('django.db.models.fields.IntegerField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tank': ('django.db.models.fields.IntegerField', [], {'max_length': '200'}),
            'teammate': ('django.db.models.fields.IntegerField', [], {'max_length': '200'}),
            'topics': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'topic_requirement'", 'to': u"orm['teammate.Topic']"})
        },
        u'teammate.skill': {
            'Meta': {'object_name': 'Skill'},
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['teammate.Game']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'teammate.topic': {
            'Instance': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['teammate.Instance']"}),
            'Meta': {'object_name': 'Topic'},
            'chatroom': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'game_name': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'topic_game'", 'to': u"orm['teammate.Game']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner_name': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'topic_targets'", 'to': u"orm['auth.User']"}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'max_length': '200'}),
            'remark': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'teammate.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'attitude': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'chatroom': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'userprofile_chatroom'", 'null': 'True', 'to': u"orm['teammate.Chatroom']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'facebook_id': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'user_profile'", 'unique': 'True', 'to': u"orm['auth.User']"})
        },
        u'teammate.usertype': {
            'Meta': {'object_name': 'UserType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'type': ('django.db.models.fields.IntegerField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['teammate']