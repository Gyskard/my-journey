create table location
(
    id                  serial
        constraint location_pk
            primary key,
    house_number_street integer,
    street_name         varchar,
    city                varchar,
    county              varchar,
    postal_code         integer
);

alter table location
    owner to admin;

create table note
(
    id          integer default nextval('notes_id_seq'::regclass) not null
        constraint notes_pk
            primary key,
    description varchar                                           not null,
    date        date                                              not null,
    location_id integer                                           not null
        constraint note_location_id_fkey
            references location
);

alter table note
    owner to admin;

create unique index notes_id_uindex
    on note (id);

create unique index location_id_uindex
    on location (id);

create table person
(
    id         serial
        constraint person_pk
            primary key,
    first_name varchar not null,
    last_name  varchar not null
);

alter table person
    owner to admin;

create unique index person_id_uindex
    on person (id);

create table participation
(
    note_id   integer
        constraint participation_note_id_fkey
            references note,
    person_id integer
        constraint participation_person_id_fkey
            references person
);

alter table participation
    owner to admin;

