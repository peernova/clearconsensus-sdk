/*
 * clearconsensus-sdk
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.model;

import java.util.Objects;
import java.util.Arrays;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import org.openapitools.client.model.TitaniumNameAliasPair;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonArray;
import com.google.gson.JsonDeserializationContext;
import com.google.gson.JsonDeserializer;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParseException;
import com.google.gson.TypeAdapterFactory;
import com.google.gson.reflect.TypeToken;

import java.lang.reflect.Type;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Set;

import org.openapitools.client.JSON;

/**
 * TitaniumGenericChartMetadata
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2023-11-09T12:11:20.940336Z[UTC]")
public class TitaniumGenericChartMetadata {
  public static final String SERIALIZED_NAME_FILTER = "filter";
  @SerializedName(SERIALIZED_NAME_FILTER)
  private String filter;

  public static final String SERIALIZED_NAME_GROUP_BY = "groupBy";
  @SerializedName(SERIALIZED_NAME_GROUP_BY)
  private List<TitaniumNameAliasPair> groupBy = null;

  public static final String SERIALIZED_NAME_METRICS = "metrics";
  @SerializedName(SERIALIZED_NAME_METRICS)
  private List<TitaniumNameAliasPair> metrics = null;

  public static final String SERIALIZED_NAME_ROW_LIMIT = "rowLimit";
  @SerializedName(SERIALIZED_NAME_ROW_LIMIT)
  private Integer rowLimit;

  public static final String SERIALIZED_NAME_SELECT_FIELDS = "selectFields";
  @SerializedName(SERIALIZED_NAME_SELECT_FIELDS)
  private List<TitaniumNameAliasPair> selectFields = null;

  public static final String SERIALIZED_NAME_SERIES_LIMIT = "seriesLimit";
  @SerializedName(SERIALIZED_NAME_SERIES_LIMIT)
  private Integer seriesLimit;

  public static final String SERIALIZED_NAME_SORT_BY = "sortBy";
  @SerializedName(SERIALIZED_NAME_SORT_BY)
  private String sortBy;

  public TitaniumGenericChartMetadata() { 
  }

  public TitaniumGenericChartMetadata filter(String filter) {
    
    this.filter = filter;
    return this;
  }

   /**
   * Get filter
   * @return filter
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getFilter() {
    return filter;
  }


  public void setFilter(String filter) {
    this.filter = filter;
  }


  public TitaniumGenericChartMetadata groupBy(List<TitaniumNameAliasPair> groupBy) {
    
    this.groupBy = groupBy;
    return this;
  }

  public TitaniumGenericChartMetadata addGroupByItem(TitaniumNameAliasPair groupByItem) {
    if (this.groupBy == null) {
      this.groupBy = new ArrayList<>();
    }
    this.groupBy.add(groupByItem);
    return this;
  }

   /**
   * Get groupBy
   * @return groupBy
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public List<TitaniumNameAliasPair> getGroupBy() {
    return groupBy;
  }


  public void setGroupBy(List<TitaniumNameAliasPair> groupBy) {
    this.groupBy = groupBy;
  }


  public TitaniumGenericChartMetadata metrics(List<TitaniumNameAliasPair> metrics) {
    
    this.metrics = metrics;
    return this;
  }

  public TitaniumGenericChartMetadata addMetricsItem(TitaniumNameAliasPair metricsItem) {
    if (this.metrics == null) {
      this.metrics = new ArrayList<>();
    }
    this.metrics.add(metricsItem);
    return this;
  }

   /**
   * Get metrics
   * @return metrics
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public List<TitaniumNameAliasPair> getMetrics() {
    return metrics;
  }


  public void setMetrics(List<TitaniumNameAliasPair> metrics) {
    this.metrics = metrics;
  }


  public TitaniumGenericChartMetadata rowLimit(Integer rowLimit) {
    
    this.rowLimit = rowLimit;
    return this;
  }

   /**
   * Get rowLimit
   * @return rowLimit
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Integer getRowLimit() {
    return rowLimit;
  }


  public void setRowLimit(Integer rowLimit) {
    this.rowLimit = rowLimit;
  }


  public TitaniumGenericChartMetadata selectFields(List<TitaniumNameAliasPair> selectFields) {
    
    this.selectFields = selectFields;
    return this;
  }

  public TitaniumGenericChartMetadata addSelectFieldsItem(TitaniumNameAliasPair selectFieldsItem) {
    if (this.selectFields == null) {
      this.selectFields = new ArrayList<>();
    }
    this.selectFields.add(selectFieldsItem);
    return this;
  }

   /**
   * Get selectFields
   * @return selectFields
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public List<TitaniumNameAliasPair> getSelectFields() {
    return selectFields;
  }


  public void setSelectFields(List<TitaniumNameAliasPair> selectFields) {
    this.selectFields = selectFields;
  }


  public TitaniumGenericChartMetadata seriesLimit(Integer seriesLimit) {
    
    this.seriesLimit = seriesLimit;
    return this;
  }

   /**
   * Get seriesLimit
   * @return seriesLimit
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Integer getSeriesLimit() {
    return seriesLimit;
  }


  public void setSeriesLimit(Integer seriesLimit) {
    this.seriesLimit = seriesLimit;
  }


  public TitaniumGenericChartMetadata sortBy(String sortBy) {
    
    this.sortBy = sortBy;
    return this;
  }

   /**
   * Get sortBy
   * @return sortBy
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getSortBy() {
    return sortBy;
  }


  public void setSortBy(String sortBy) {
    this.sortBy = sortBy;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TitaniumGenericChartMetadata titaniumGenericChartMetadata = (TitaniumGenericChartMetadata) o;
    return Objects.equals(this.filter, titaniumGenericChartMetadata.filter) &&
        Objects.equals(this.groupBy, titaniumGenericChartMetadata.groupBy) &&
        Objects.equals(this.metrics, titaniumGenericChartMetadata.metrics) &&
        Objects.equals(this.rowLimit, titaniumGenericChartMetadata.rowLimit) &&
        Objects.equals(this.selectFields, titaniumGenericChartMetadata.selectFields) &&
        Objects.equals(this.seriesLimit, titaniumGenericChartMetadata.seriesLimit) &&
        Objects.equals(this.sortBy, titaniumGenericChartMetadata.sortBy);
  }

  @Override
  public int hashCode() {
    return Objects.hash(filter, groupBy, metrics, rowLimit, selectFields, seriesLimit, sortBy);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TitaniumGenericChartMetadata {\n");
    sb.append("    filter: ").append(toIndentedString(filter)).append("\n");
    sb.append("    groupBy: ").append(toIndentedString(groupBy)).append("\n");
    sb.append("    metrics: ").append(toIndentedString(metrics)).append("\n");
    sb.append("    rowLimit: ").append(toIndentedString(rowLimit)).append("\n");
    sb.append("    selectFields: ").append(toIndentedString(selectFields)).append("\n");
    sb.append("    seriesLimit: ").append(toIndentedString(seriesLimit)).append("\n");
    sb.append("    sortBy: ").append(toIndentedString(sortBy)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }


  public static HashSet<String> openapiFields;
  public static HashSet<String> openapiRequiredFields;

  static {
    // a set of all properties/fields (JSON key names)
    openapiFields = new HashSet<String>();
    openapiFields.add("filter");
    openapiFields.add("groupBy");
    openapiFields.add("metrics");
    openapiFields.add("rowLimit");
    openapiFields.add("selectFields");
    openapiFields.add("seriesLimit");
    openapiFields.add("sortBy");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

 /**
  * Validates the JSON Object and throws an exception if issues found
  *
  * @param jsonObj JSON Object
  * @throws IOException if the JSON Object is invalid with respect to TitaniumGenericChartMetadata
  */
  public static void validateJsonObject(JsonObject jsonObj) throws IOException {
      if (jsonObj == null) {
        if (TitaniumGenericChartMetadata.openapiRequiredFields.isEmpty()) {
          return;
        } else { // has required fields
          throw new IllegalArgumentException(String.format("The required field(s) %s in TitaniumGenericChartMetadata is not found in the empty JSON string", TitaniumGenericChartMetadata.openapiRequiredFields.toString()));
        }
      }

      Set<Entry<String, JsonElement>> entries = jsonObj.entrySet();
      // check to see if the JSON string contains additional fields
      for (Entry<String, JsonElement> entry : entries) {
        if (!TitaniumGenericChartMetadata.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TitaniumGenericChartMetadata` properties. JSON: %s", entry.getKey(), jsonObj.toString()));
        }
      }
      if (jsonObj.get("filter") != null && !jsonObj.get("filter").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `filter` to be a primitive type in the JSON string but got `%s`", jsonObj.get("filter").toString()));
      }
      JsonArray jsonArraygroupBy = jsonObj.getAsJsonArray("groupBy");
      if (jsonArraygroupBy != null) {
        // ensure the json data is an array
        if (!jsonObj.get("groupBy").isJsonArray()) {
          throw new IllegalArgumentException(String.format("Expected the field `groupBy` to be an array in the JSON string but got `%s`", jsonObj.get("groupBy").toString()));
        }

        // validate the optional field `groupBy` (array)
        for (int i = 0; i < jsonArraygroupBy.size(); i++) {
          TitaniumNameAliasPair.validateJsonObject(jsonArraygroupBy.get(i).getAsJsonObject());
        };
      }
      JsonArray jsonArraymetrics = jsonObj.getAsJsonArray("metrics");
      if (jsonArraymetrics != null) {
        // ensure the json data is an array
        if (!jsonObj.get("metrics").isJsonArray()) {
          throw new IllegalArgumentException(String.format("Expected the field `metrics` to be an array in the JSON string but got `%s`", jsonObj.get("metrics").toString()));
        }

        // validate the optional field `metrics` (array)
        for (int i = 0; i < jsonArraymetrics.size(); i++) {
          TitaniumNameAliasPair.validateJsonObject(jsonArraymetrics.get(i).getAsJsonObject());
        };
      }
      JsonArray jsonArrayselectFields = jsonObj.getAsJsonArray("selectFields");
      if (jsonArrayselectFields != null) {
        // ensure the json data is an array
        if (!jsonObj.get("selectFields").isJsonArray()) {
          throw new IllegalArgumentException(String.format("Expected the field `selectFields` to be an array in the JSON string but got `%s`", jsonObj.get("selectFields").toString()));
        }

        // validate the optional field `selectFields` (array)
        for (int i = 0; i < jsonArrayselectFields.size(); i++) {
          TitaniumNameAliasPair.validateJsonObject(jsonArrayselectFields.get(i).getAsJsonObject());
        };
      }
      if (jsonObj.get("sortBy") != null && !jsonObj.get("sortBy").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `sortBy` to be a primitive type in the JSON string but got `%s`", jsonObj.get("sortBy").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TitaniumGenericChartMetadata.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TitaniumGenericChartMetadata' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TitaniumGenericChartMetadata> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TitaniumGenericChartMetadata.class));

       return (TypeAdapter<T>) new TypeAdapter<TitaniumGenericChartMetadata>() {
           @Override
           public void write(JsonWriter out, TitaniumGenericChartMetadata value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TitaniumGenericChartMetadata read(JsonReader in) throws IOException {
             JsonObject jsonObj = elementAdapter.read(in).getAsJsonObject();
             validateJsonObject(jsonObj);
             return thisAdapter.fromJsonTree(jsonObj);
           }

       }.nullSafe();
    }
  }

 /**
  * Create an instance of TitaniumGenericChartMetadata given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of TitaniumGenericChartMetadata
  * @throws IOException if the JSON string is invalid with respect to TitaniumGenericChartMetadata
  */
  public static TitaniumGenericChartMetadata fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TitaniumGenericChartMetadata.class);
  }

 /**
  * Convert an instance of TitaniumGenericChartMetadata to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

