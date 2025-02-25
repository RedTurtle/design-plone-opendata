import React from 'react';
import cx from 'classnames';
import {
  SearchSectionForm,
  PageHeaderNav,
  RelatedItems,
  PagePlaceholderAfterContent,
  PagePlaceholderAfterRelatedItems,
  PagePlaceholderTitle,
  TextOrBlocks,
  RichText,
  RelatedItemInEvidence,
  richTextHasContent,
  PageHeaderTassonomiaArgomenti,
  Sharing,
  Actions,
  PageMetadata,
} from 'design-comuni-plone-theme/components/ItaliaTheme/View';
import { defineMessages, useIntl } from 'react-intl';
import { getLayoutFieldname } from '@plone/volto/helpers';
import config from '@plone/volto/registry';
import { Chip, ChipLabel, Card, CardBody, CardTitle, CardCategory, Container, Icon } from 'design-react-kit';
import { flattenToAppURL } from '@plone/volto/helpers';
import {
  RichTextSection,
  OfficeCard,
} from 'design-comuni-plone-theme/components/ItaliaTheme/View';

const messages = defineMessages({
  frequency: {
    id: 'freqency',
    defaultMessage: 'Frequenza di aggiornamento',
  },
  themes: {
    id: 'themes',
    defaultMessage: 'Temi',
  },
  attachment: {
    id: 'attachment',
    defaultMessage: 'Allegato',
  },
  last_update_date : {
    id: 'last_update_date',
    defaultMessage: 'Data ultimo aggiornamento',  
  },
  release_date: {
    id: 'release_date',
    defaultMessage: 'Data rilascio',
  },
});

// https://italia.github.io/design-react-kit/?path=/docs/documentazione-utilities-icon--documentazione#lista-delle-icone-disponibili
const icons = {
  'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet': 'it-file-sheet',
  'application/vnd.oasis.opendocument.text': 'it-file-odt',
};

const types = {
  'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet': 'Excel XLSX',
  'application/vnd.oasis.opendocument.text': 'ODT',
  'text/csv': 'CSV',
}

/**
 * PageView view component class.
 * @function PageView
 * @params {object} content Content object.
 * @returns {string} Markup of the component.
 */
const PageView = ({ content, token, location, history }) => {
  const intl = useIntl();
  // const documentBody = createRef();
  // const { sideMenuElements, SideMenu } = useSideMenu(content, documentBody);


  const Image = config.getComponent({ name: 'Image' }).component;
  const rightHeaderHasContent =
    content.image?.scales ||
    richTextHasContent(content.info_testata) ||
    content.mostra_navigazione ||
    content?.tassonomia_argomenti?.length > 0 ||
    content.mostra_bottoni_condivisione;

  return (
    <>
      <div id="page-document" className="ui container px-4">
          <div className="PageHeaderWrapper mb-4">
          <div className="row">
            <div
              className={cx('title-description-wrapper', {
                'col-lg-6': rightHeaderHasContent,
                'col-lg-12': !rightHeaderHasContent,
              })}
            >
              <PagePlaceholderTitle content={content}>
                <h1 className="mb-3" data-element="page-name">
                  {content?.title}
                </h1>
              </PagePlaceholderTitle>

              <p className="description">{content?.description}</p>
              {content?.ricerca_in_testata && (
                <SearchSectionForm content={content} />
              )}
            </div>
            {/* {rightHeaderHasContent && (
                <div className="col-lg-4 offset-lg-2">
                  {content.mostra_bottoni_condivisione && (
                    <div className="px-4 mb-4">
                      <Sharing url={content['@id']} title={content.title} />
                      <Actions url={content['@id']} title={content.title} />
                    </div>
                  )}
                  {content.image && (
                    <div className="header-image px-4 mb-3">
                      <Image
                        item={content}
                        alt=""
                        sizes="250px"
                        responsive={true}
                      />
                    </div>
                  )}
                  {richTextHasContent(content.info_testata) && (
                    <div className="header-infos px-4 mb-5">
                      <RichText serif={false} data={content.info_testata} />
                    </div>
                  )}

                  {content.mostra_navigazione && (
                    <PageHeaderNav
                      content={content}
                      title={intl.formatMessage(messages.inThisSection)}
                    />
                  )}
                  {content?.tassonomia_argomenti?.length > 0 && (
                    <div className="px-4">
                      <PageHeaderTassonomiaArgomenti content={content} />
                    </div>
                  )}
                </div>
              )} */}
          </div>
        </div>

        <h5>Data e Risorse</h5>
        <Container>
          {content.items.filter((item) => item['@type'] === 'File').map((item, idx) =>
            <>
              <h6>
                {/* <Icon className="icon-primary" icon={icons[item.mime_type]}></Icon> */}
                <a href={flattenToAppURL(`${item.url}/@@download/file`)}>
                  {item.title}{' '}
                  ({item.getObjSize})
                </a>
              </h6>
              <Container>
              <dl class="row">
              <dt>Licenza</dt><dd>{content.license?.title}</dd>
              <dt>Formato</dt><dd>{types[item.mime_type] ?? item.mime_type}</dd>
              {item.description && <><dt>Descrizione</dt><dd>{item.description}</dd></>}
              </dl>
              </Container>
            </>
          )}

        </Container>

        <h5>Metadati del Dataset</h5>
        <Container>
          <dl className="row">
          {content.release_date &&  <>
              <dt>{intl.formatMessage(messages.release_date)}</dt>
              <dd>{new Date(content.release_date)}</dd>
            </>}
            {content.last_update_date &&  <>
              <dt>{intl.formatMessage(messages.last_update_date)}</dt>
              <dd>{content.last_update_date}</dd>
            </>}
            {content.frequency && <>
              <dt>{intl.formatMessage(messages.frequency)}</dt>
              <dd>{content.frequency.title}</dd>
            </>}
            {content.themes && <>
              <dt>{intl.formatMessage(messages.themes)}</dt>
              <dd>{content.themes.map((t, idx) =>
                <Chip
                  color=""
                  disabled={true}
                  large={false}
                  simple    
                  tag="div"
                  key={idx}
                  className="me-2"
                >
                  <ChipLabel tag="span">{t.title}</ChipLabel>
                </Chip>
              )}</dd>
            </>}
          </dl>
        </Container>

      <h5>Titolare</h5>
        <div className="card-wrapper card-teaser-wrapper card-teaser-wrapper-equal">
        {content.rightsHolder?.length > 0 && (
          <>
            {content.rightsHolder.map((item) => (
              <OfficeCard key={item['@id']} office={item} />
            ))}
          </>
        )}
      </div>



        <TextOrBlocks content={content} />

        <pre>{JSON.stringify(content, null, 2)}</pre>

        {content.show_modified && <PageMetadata content={content} />}
      </div>

      <PagePlaceholderAfterContent content={content} />
      <RelatedItems content={content} />
      <RelatedItemInEvidence content={content} />
      <PagePlaceholderAfterRelatedItems content={content} />
    </>
  );

};

export default PageView;
