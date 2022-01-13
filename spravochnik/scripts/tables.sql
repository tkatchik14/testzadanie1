drop  schema if exists nsi cascade
;
create schema nsi
;
comment on schema nsi is 'объекты НСИ'
;
create table nsi.dictionary
(
    id serial constraint pk_dictionary_id primary key,
    sprid varchar(10) not null ,
    name varchar(150) not null ,
    shortname varchar(50),
    description varchar(1000),
    version varchar(5) not null ,
    datefrom  date not null default current_date,
    dateto  date,
    constraint un_dictionary_sprid_version unique (sprid, version)
)
;
comment on table nsi.dictionary is 'Таблица справочников'
;
comment on column nsi.dictionary.id is 'первичный ключ'
;
comment on column nsi.dictionary.sprid is 'идентификатор справочника'
;
comment on column nsi.dictionary.name is 'наименование'
;
comment on column nsi.dictionary.shortname is 'короткое наименование'
;
comment on column nsi.dictionary.description is 'описание'
;
comment on column nsi.dictionary.version is 'версия'
;
comment on column nsi.dictionary.datefrom is 'дата начала действия справочника этой версии'
;
comment on column nsi.dictionary.dateto is 'дата конца действия справочника этой версии, если null то актуальный'
;
create table nsi.dictionary_item
(
    id serial constraint pk_dictionary_item_id primary key,
    dictionary_id integer not null ,
    parent_id integer,
    item_code varchar(10) not null ,
    item_value varchar(100) not null,
    constraint un_dict_code_value unique (dictionary_id, item_code),
    constraint fk_dict_item_id foreign key (dictionary_id) references nsi.dictionary (id) on delete cascade

);
comment on table nsi.dictionary_item is 'Элемент справочника'
;
comment on column nsi.dictionary_item.id is 'идентификатор'
;
comment on column nsi.dictionary_item.dictionary_id is 'ссылка на справочник'
;
comment on column nsi.dictionary_item.parent_id is 'родительский идентификатор'
;
comment on column nsi.dictionary_item.item_code is 'код элемента'
;
comment on column nsi.dictionary_item.item_value is 'значение элемента'
;
create index ix_dictionary_id on nsi.dictionary_item (dictionary_id)
;
grant all on nsi.dictionary to nsi_user;