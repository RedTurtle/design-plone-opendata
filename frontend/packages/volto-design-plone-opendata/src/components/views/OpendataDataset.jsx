import {
  ContentTypeViewSections,
  OfficeCard,
  PageHeader,
  PageMetadata,
  PagePlaceholderAfterContent,
  PagePlaceholderAfterRelatedItems,
  RelatedItemInEvidence,
  RelatedItems,
  RichTextSection,
  SkipToMainContent,
  TextOrBlocks,
  useSideMenu,
} from 'design-comuni-plone-theme/components/ItaliaTheme/View';
import { Chip, ChipLabel, Container } from 'design-react-kit';
import React, { createRef } from 'react';
import { defineMessages, useIntl } from 'react-intl';

import { flattenToAppURL } from '@plone/volto/helpers';

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
  last_update_date: {
    id: 'last_update_date',
    defaultMessage: 'Data ultimo aggiornamento',
  },
  release_date: {
    id: 'release_date',
    defaultMessage: 'Data rilascio',
  },
  distributions: {
    id: 'dataset_distributions',
    defaultMessage: 'Data e risorse',
  },
  metadata: {
    id: 'dataset_metadata',
    defaultMessage: 'Metadati del Dataset',
  },
  holder: {
    id: 'dataset_holder',
    defaultMessage: 'Titolare',
  },
});

// https://italia.github.io/design-react-kit/?path=/docs/documentazione-utilities-icon--documentazione#lista-delle-icone-disponibili
// const icons = {
//   'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet': 'it-file-sheet',
//   'application/vnd.oasis.opendocument.text': 'it-file-odt',
// };

const types = {
  'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
    'Excel XLSX',
  'application/vnd.oasis.opendocument.text': 'ODT',
  'text/csv': 'CSV',
};

const Distributions = ({ content }) => {
  const intl = useIntl();

  return (
    <RichTextSection
      tag_id={'dataset-distributions'}
      title={intl.formatMessage(messages.distributions)}
    >
      <div className="card-wrapper card-teaser-wrapper card-teaser-wrapper-equal">
        {content.items
          .filter((item) => item['@type'] === 'File')
          .map((item, idx) => (
            <>
              <h6>
                {/* <Icon className="icon-primary" icon={icons[item.mime_type]}></Icon> */}
                <a href={flattenToAppURL(`${item.url}/@@download/file`)}>
                  {`${item.title} (${item.getObjSize})`}
                </a>
              </h6>
              <Container>
                <dl class="row">
                  <dt>Licenza</dt>
                  <dd>{content.license?.title}</dd>
                  <dt>Formato</dt>
                  <dd>{types[item.mime_type] ?? item.mime_type}</dd>
                  {item.description && (
                    <>
                      <dt>Descrizione</dt>
                      <dd>{item.description}</dd>
                    </>
                  )}
                </dl>
              </Container>
            </>
          ))}
      </div>
    </RichTextSection>
  );
};

const Metadata = ({ content }) => {
  const intl = useIntl();

  return (
    <RichTextSection
      tag_id={'dataset-metadata'}
      title={intl.formatMessage(messages.metadata)}
    >
      <div className="card-wrapper card-teaser-wrapper card-teaser-wrapper-equal">
        <dl className="row">
          {content.release_date && (
            <>
              <dt>{intl.formatMessage(messages.release_date)}</dt>
              <dd>{intl.formatDate(content.release_date)}</dd>
              {/* intl.formatTime(content.release_date) */}
            </>
          )}
          {content.last_update_date && (
            <>
              <dt>{intl.formatMessage(messages.last_update_date)}</dt>
              <dd>{intl.formatDate(content.last_update_date)}</dd>
              {/* intl.formatTime(content.last_update_date) */}
            </>
          )}
          {content.frequency && (
            <>
              <dt>{intl.formatMessage(messages.frequency)}</dt>
              <dd>{content.frequency.title}</dd>
            </>
          )}
          {content.themes && (
            <>
              <dt>{intl.formatMessage(messages.themes)}</dt>
              <dd>
                {content.themes.map((t, idx) => (
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
                ))}
              </dd>
            </>
          )}
        </dl>
      </div>
    </RichTextSection>
  );
};

const Holder = ({ content }) => {
  const intl = useIntl();
  return (
    content.rightsHolder?.length > 0 && (
      <RichTextSection
        tag_id={'dataset-holder'}
        title={intl.formatMessage(messages.holder)}
      >
        <div className="card-wrapper card-teaser-wrapper card-teaser-wrapper-equal">
          {content.rightsHolder.map((item) => (
            <OfficeCard key={item['@id']} office={item} />
          ))}
        </div>
      </RichTextSection>
    )
  );
};

const SectionsOrder = [
  { component: Distributions },
  { component: Metadata },
  { component: Holder },
];

/**
 * PageView view component class.
 * @function PageView
 * @params {object} content Content object.
 * @returns {string} Markup of the component.
 */
const PageView = ({ content, token, location, history }) => {
  const documentBody = createRef();
  const { sideMenuElements, SideMenu } = useSideMenu(content, documentBody);

  return (
    <>
      <div className="container px-4 my-4 documento-view">
        <SkipToMainContent />
        <PageHeader
          content={content}
          readingtime={null}
          showtassonomiaargomenti={true}
        />
        <div className="row row-column-border border-light row-column-menu-left">
          <aside className="col-lg-4">
            {__CLIENT__ && (
              <SideMenu data={sideMenuElements} content_uid={content?.UID} />
            )}
          </aside>
          <section
            ref={documentBody}
            id="main-content-section"
            className="col-lg-8 it-page-sections-container border-light"
          >
            <ContentTypeViewSections
              content={content}
              defaultSections={SectionsOrder}
            />
          </section>
        </div>
      </div>

      <TextOrBlocks content={content} />

      {/* <pre>{JSON.stringify(content, null, 2)}</pre> */}

      {content.show_modified && <PageMetadata content={content} />}
      <PagePlaceholderAfterContent content={content} />
      <RelatedItems content={content} />
      <RelatedItemInEvidence content={content} />
      <PagePlaceholderAfterRelatedItems content={content} />
    </>
  );
};

export default PageView;
